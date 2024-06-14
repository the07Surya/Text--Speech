import pyttsx3
#We will now initiate the ‘init’ function in order to get an engine instance
engine = pyttsx3.init()
#Using the ‘say’ method on the engine, we input text we wish to be spoken
engine.say("Hi Surya! I Love U")
#We now use the ‘run and wait’ method to process the voice commands
engine.runAndWait()




