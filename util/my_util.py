from IPython.core.display import HTML
import numpy as np
# wavPlayer('a.wav')
# wavPlayer('fooX.wav')
def wavPlayer(filepath):

    src = """
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Simple Test</title>
    </head>
    
    <body>
    <audio controls="controls" style="width:600px" >
      <source src="files/%s" type="audio/wav" />
      Your browser does not support the audio element.
    </audio>
    </body>
    """%(filepath)
    display(HTML(src))
def note2f0(n):
    return 440.0*np.power(2,(n-49)/12.0)
def f02note(f0):
    return 12*np.log2(f0/440)+49
