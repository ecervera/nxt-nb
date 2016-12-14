import nxt.bluesock
import nxt.motor
import nxt.sensor

from bluetooth.btcommon import BluetoothError

Motor = nxt.motor.Motor
PORT_A = nxt.motor.PORT_A
PORT_B = nxt.motor.PORT_B
PORT_C = nxt.motor.PORT_C

Touch = nxt.sensor.Touch
Light = nxt.sensor.Light
Ultrasonic = nxt.sensor.Ultrasonic

PORT_1 = nxt.sensor.PORT_1
PORT_2 = nxt.sensor.PORT_2
PORT_3 = nxt.sensor.PORT_3
PORT_4 = nxt.sensor.PORT_4

def connectar(n):
    try:
        address = {5: '00:16:53:08:D5:59', 12: '00:16:53:1A:C6:BD'}
        return nxt.bluesock.BlueSock(address[n]).connect()
    except BluetoothError as e:
        errno, errmsg = eval(e.args[0])
        if errno==16:
            print("No es pot connectar, ja hi ha un altre programa. Has de desconnectar-lo abans!")
        elif errno==13:
            print("No es pot connectar, el dispositiu no està emparellat.")
        elif errno == 112:
            print("No es troba el brick, assegurat que estiga encés.")
        else:
            print("Error %d: %s" % (errno, errmsg))

def desconnectar(brick):
    brick.sock.close()

class Sound():
    def __init__(self,brick):
        self._brick = brick
        
    def _play(self,str):
        self._brick.play_sound_file(False, bytes((str+'.rso').encode('ascii')))
        
    def click(self):
        self._play('! Click')
        
    def startup(self):
        self._play('! Startup')
        
    def error(self):
        self._play('! Error 02')
        
    def applause(self):
        self._play('! Applause')
        
    def arm(self):
        self._play('! Arm 09')
        
    def attention(self):
        self._play('! Attention')
        
class Say():
    def __init__(self,brick):
        self._brick = brick
        
    def _say(self,str):
        self._brick.play_sound_file(False, bytes((str+'.rso').encode('ascii')))
        
    def hello(self):
        self._say('Hello')
        
    def youre_good(self):
        self._say("You're Good")
        
    def good_job(self):
        self._say('Good Job')
        
    def have_a_nice_day(self):
        self._say('Have A Nice Day')
        
    def hot(self):
        self._say('Hot')
        
    def thank_you(self):
        self._say('Thank You')
        
    def woops(self):
        self._say('Woops')
        
    def game_over(self):
        self._say('Game Over')
        
    def sorry(self):
        self._say('Sorry')
        
    def object_detected(self):
        self._say('Object Detected')
        
    def music(self):
        self._say('Music')
        
    def system_overload(self):
        self._say('System Overload')
        
    def buuuhh(self):
        self._say('Buuuhh')
        
    def green(self):
        self._say('Green')
        
import math
import time

def Musica(brick):
    global _brick
    global _tempo
    _brick = brick
    _tempo = 0.5
        
def _freq(fbase,octava):
        if octava == 0:
            return int(fbase)
        else:
            return int(fbase*math.pow(2,octava))
        
def _play(f,t):
    try:
        _brick.play_tone_and_wait(f, int(t*1000*_tempo))
        time.sleep(0.01)
    except:
        pass
    
def Silenci(t=1):
    time.sleep(t)
    
def Do(t=1, octava=0):
        f = _freq(261.63,octava)
        _play(f,t)

def Re(t=1, octava=0):
        f = _freq(293.66,octava)
        _play(f,t)

def Mi(t=1, octava=0):
        f = _freq(329.63,octava)
        _play(f,t)

def Fa(t=1, octava=0):
        f = _freq(349.23,octava)
        _play(f,t)
        
def Sol(t=1, octava=0):
        f = _freq(392.00,octava)
        _play(f,t)
        
def La(t=1, octava=0):
        f = _freq(440.00,octava)
        _play(f,t)

def Si_bemol(t=1, octava=0):
        f = _freq(466.16,octava)
        _play(f,t)

def Si(t=1, octava=0):
        f = _freq(493.88,octava)
        _play(f,t)
