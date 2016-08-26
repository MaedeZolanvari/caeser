#from string import letters
import cgi
import webapp2

from caesar import encrypt
from sys import argv, exit
from helpers import alpha_position, rotate_character

class Index(webapp2.RequestHandler):
    form = """
    <form method="post">
        <label>
        I want to rot13 encrypt
        <input type="text" name ="old_string"/>
        this text
        </label>
        <label for ="rot"> Rotate by: </label>
        <input type="text" name ="rot"/>
        <input type="submit" value="Encrypt"/>
    </form>
    """
    def get(self):
        self.response.out.write(self.form)

    def post(self):
        old_string = self.request.get("old_string")
        old_string = cgi.escape (old_string)
        rot = self.request.get("rot")
        rotint = int(rot)
        new_string = encrypt(old_string,rotint)
        self.response.out.write("<p>" + old_string + " is the unencrypted version of your word!"+"</p>")
        self.response.out.write("<p>"+new_string + " is the encrypted version of your word!"+"</p>")


#class Rot13(webapp2.RequestHandler):
#    def get(self):
#        input_form = """
#        <form method="post">
#            <lable for ="rot"> Rotate by: </lable>
#            <input type="text" name ="rot" value="0">
#            <p class="error"></p>
#            <textarea type="text" name="text"
#                    style="height: 100px; width: 400px;"></textarea>
#            <br>
#            <input type="submit">
#        </form>
#        """
#
#    def post(self):
#        rot13 = ''
#        text = self.request.get('text')
#        text2 = cgi.escape(text)
#        if text2:
#            rot13 = text2.encode('rot13')
#        output_form = """
#        <form method="post">
#            <textarea name="text"
#                    style="height: 100px; width: 400px;">rot13</textarea>
#            <br>
#            <input type="submit">
#        </form>
#        """


app = webapp2.WSGIApplication([('/', Index)
                              ],debug=True)
