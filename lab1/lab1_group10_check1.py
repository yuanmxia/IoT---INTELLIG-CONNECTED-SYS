import esp
import machine
from machine import Pin
import time

p0 = Pin(0, Pin.OUT)

def S():
    p0.off()                 # set pin to "on" (high) level
    time.sleep_ms(300)
    p0.on()                # set pin to "off" (low) level
    time.sleep_ms(300)
    p0.off()                 # set pin to "on" (high) level
    time.sleep_ms(300)
    p0.on()                # set pin to "off" (low) level
    time.sleep_ms(300)
    p0.off()                 # set pin to "on" (high) level
    time.sleep_ms(300)
    p0.on()                # set pin to "off" (low) level
    time.sleep_ms(300)

def O():
    p0.off()                 # set pin to "on" (high) level
    time.sleep_ms(600)
    p0.on()                # set pin to "off" (low) level
    time.sleep_ms(600)
    p0.off()                 # set pin to "on" (high) level
    time.sleep_ms(600)
    p0.on()                # set pin to "off" (low) level
    time.sleep_ms(600)
    p0.off()                 # set pin to "on" (high) level
    time.sleep_ms(600)
    p0.on()                # set pin to "off" (low) level
    time.sleep_ms(600)

while True:
    S()
    O()
    S()
    time.sleep(3)
