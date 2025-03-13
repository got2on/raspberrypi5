from gpiozero import LED
import time
import random

red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)

def stop_light(traffic_status):
    print("Red Light: ON")
    if traffic_status['red_LED']:
        red_led.on()
    else:
        red_led.off()

def yield_light(traffic_status):
    print("Yellow Light: ON")
    if traffic_status['yellow_LED']:
        yellow_led.on()
    else:
        yellow_led.off()

def go_light(traffic_status):
    print("Green Light: ON")
    if traffic_status['green_LED']:
        green_led.on()
    else:
        green_led.off()

def main():
    
    traffic_light = {'red_LED': 0, 'yellow_LED': 0, 'green_LED': 1}
    
    while True:
        status = random.choice(list(traffic_light.keys()))
        print(f"Randomly chosen light: {status}")

        red_led.off()
        yellow_led.off()
        green_led.off()

        if status == 'red_LED':
            traffic_light['red_LED'] = 1
            stop_light(traffic_light)
        elif status == 'yellow_LED':
            traffic_light['yellow_LED'] = 1
            yield_light(traffic_light)
        elif status == 'green_LED':
            traffic_light['green_LED'] = 1
            go_light(traffic_status=traffic_light)


        time.sleep(10)

main()