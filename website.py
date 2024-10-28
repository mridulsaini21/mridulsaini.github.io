import http.server
from http.server import SimpleHTTPRequestHandler
import socketserver

# HTML content for each page with inline CSS for styling
pages = {
    "/": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Our Story</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; color: #fff; background-image: url('https://example.com/your_image1.jpg'); background-size: cover; background-position: center; position: relative; height: 100vh; overflow: hidden; }
            h1 { color: #f0f8ff; }
            .image-box { width: 150px; height: 150px; background-color: rgba(255, 255, 255, 0.8); border-radius: 10px; margin: 10px; position: absolute; }
            .image-box img { width: 100%; height: 100%; border-radius: 10px; }
            .image-text { position: absolute; bottom: 5px; left: 5px; color: #333; font-size: 0.9em; }
            .button { background-color: #4682B4; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin-top: 20px; position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); }
        </style>
    </head>
    <body>
        <h1>Our Story</h1>
        <div class="image-container">
            <div class="image-box" style="top: 20%; left: 10%;">
                <img src="https://example.com/picture1.jpg" alt="Picture 1">
                <div class="image-text">Text for picture 1</div>
            </div>
            <div class="image-box" style="top: 30%; left: 40%;">
                <img src="https://example.com/picture2.jpg" alt="Picture 2">
                <div class="image-text">Text for picture 2</div>
            </div>
            <div class="image-box" style="top: 50%; left: 70%;">
                <img src="https://example.com/picture3.jpg" alt="Picture 3">
                <div class="image-text">Text for picture 3</div>
            </div>
            <div class="image-box" style="top: 70%; left: 20%;">
                <img src="https://example.com/picture4.jpg" alt="Picture 4">
                <div class="image-text">Text for picture 4</div>
            </div>
            <div class="image-box" style="top: 80%; left: 60%;">
                <img src="https://example.com/picture5.jpg" alt="Picture 5">
                <div class="image-text">Text for picture 5</div>
            </div>
        </div>
        <a href="/why" class="button">Continue Our Journey</a>
    </body>
    </html>
    """,
    "/why": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Why I Love You</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; color: #fff; background-image: url('https://example.com/your_image2.jpg'); background-size: cover; background-position: center; padding: 20px; }
            h1 { color: #FF6347; }
            .points { background-color: rgba(0, 0, 0, 0.5); padding: 25px; border-radius: 10px; margin: 20px auto; display: inline-block; width: 90%; max-width: 800px; text-align: left; }
            .button { background-color: #FF6347; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin-top: 20px; display: inline-block; position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); }
        </style>
    </head>
    <body>
        <h1>Why I Love You</h1>
        <div class="points">
            <ul>
                <li>You always know how to make me smile.</li>
                <li>Your kindness and compassion inspire me.</li>
                <li>We share so many beautiful memories together.</li>
                <li>You support me in everything I do.</li>
                <li>I love your sense of adventure.</li>
                <li>Your laughter brightens my day.</li>
                <li>You have an incredible ability to see the good in people.</li>
                <li>I admire your passion for your dreams.</li>
                <li>You're my best friend and my greatest confidant.</li>
                <li>With you, I feel at home no matter where we are.</li>
            </ul>
        </div>
        <a href="/proposal" class="button">Forever and Always</a>
    </body>
    </html>
    """,
    "/proposal": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>The Proposal</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; color: #fff; background-image: url('https://example.com/your_image3.jpg'); background-size: cover; background-position: center; padding: 20px; position: relative; height: 100vh; }
            h1 { color: #32CD32; }
            .proposal-text { background-color: rgba(0, 0, 0, 0.5); padding: 25px; border-radius: 10px; margin: 20px auto; display: inline-block; width: 90%; max-width: 800px; text-align: left; }
            .button-container { display: flex; justify-content: center; position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); gap: 20px; }
            .button { background-color: #32CD32; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; }
            .button.no { background-color: #FF6347; } /* Red button for "No" option */
        </style>
    </head>
    <body>
        <h1>Will You Marry Me?</h1>
        <div class="proposal-text">
            <p>You mean the world to me, and I want to spend my life with you...</p>
            <ul>
                <li>Our love story is my favorite adventure.</li>
                <li>With you, every moment is special.</li>
                <li>I cherish the way you understand me.</li>
                <li>You make my dreams feel possible.</li>
                <li>Life is better with you by my side.</li>
                <li>You inspire me to be a better person.</li>
                <li>I love how we can talk about anything.</li>
                <li>You're my partner in everything.</li>
                <li>I can't imagine a future without you.</li>
                <li>Let's create countless memories together!</li>
            </ul>
        </div>
        <div class="button-container">
            <a href="/future" class="button">Yes</a>
            <a href="#" onclick="alert('Are you sure? Think again!')" class="button no">No</a>
        </div>
    </body>
    </html>
    """,
    "/future": """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Our Future</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; color: #fff; background-image: url('https://example.com/your_image4.jpg'); background-size: cover; background-position: center; }
            h1 { color: #8A2BE2; }
            p { font-size: 1.2em; background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px; display: inline-block; }
            .button { background-color: #8A2BE2; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin-top: 20px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Our Future Together</h1>
        <p>Here's to our dreams and all the adventures ahead...</p>
    </body>
    </html>
    """
}

# Custom handler to serve HTML content based on the URL path
class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested path is in the pages dictionary
        if self.path in pages:
            # Respond with a 200 OK status and serve the corresponding HTML page
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(pages[self.path].encode("utf-8"))
        else:
            # Respond with a 404 error if the page is not found
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - Page Not Found</h1>")

# Set the port and initialize the server
PORT = 8000  # You can change this to any open port, e.g., 8080
try:
    with socketserver.TCPServer(("localhost", PORT), CustomHandler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()
except Exception as e:
    print(f"Error starting server: {e}")
    print("Try changing the port or checking for any firewall issues.")
