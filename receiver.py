from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length)

        programs = json.loads(data.decode())

        

        for i in programs:
            print(i)

        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("mmmmmmmmmmmmm")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(data.decode())

        self.send_response(200)
        self.end_headers()

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Servas paleistas ant port 8000 ...")
server.serve_forever()