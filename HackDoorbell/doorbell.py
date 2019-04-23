from gpiozero import TonalBuzzer, Button
from picamera import PiCamera
from datetime import datetime

buzzer = TonalBuzzer(20)
doorbell = Button(21)
camera = PiCamera()

def play(tune):
    for note, duration in tune:
        buzzer.play(note)
        sleep(float(duration))
    buzzer.stop()
    
pink_panther = [
    ('C#4', 0.2), ('D4', 0.2),  (None, 0.2),
    ('Eb4', 0.2), ('E4', 0.2),  (None, 0.6),
    ('F#4', 0.2), ('G4', 0.2),  (None, 0.6),
    ('Eb4', 0.2), ('E4', 0.2),  (None, 0.2),
    ('F#4', 0.2), ('G4', 0.2),  (None, 0.2),
    ('C4', 0.2),  ('B4', 0.2),  (None, 0.2),
    ('F#4', 0.2), ('G4', 0.2),  (None, 0.2),
    ('B4', 0.2),  ('Bb4', 0.5), (None, 0.6),
    ('A4', 0.2),  ('G4', 0.2),  ('E4', 0.2),
    ('D4', 0.2),  ('E4', 0.2)
]

while True:
    doorbell.wait_for_press()
    dt = datetime.now().isoformat()
    camera.capture('/home/pi/{}.jpg'.format(dt))
    play(pink_panther)
