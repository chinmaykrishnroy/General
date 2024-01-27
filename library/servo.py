def mapping(val, upper_limit, lower_limit, max_val):
    # maps the lower_limit and upper_limit to min_val (=0) and max_val
    return lower_limit * (((val / max_val) * ((upper_limit - lower_limit) / lower_limit)) + 1)


class Servo:
    def __init__(self, servo_pin, pwm_freq=50, avg_action_time=0.5, minAngle_dutycycle=3.833, maxAngle_dutycycle=11.1388,
                 maxAngle=164.5):
        from machine import Pin, PWM
        self.pwm = PWM(Pin(servo_pin))
        self.pwm_freq = pwm_freq
        self.avg_action_time = avg_action_time
        self.minAngle_dutycycle = minAngle_dutycycle
        self.maxAngle_dutycycle = maxAngle_dutycycle
        self.maxAngle = maxAngle

    def rotation(self, angle):
        from utime import sleep
        duty_cycle = mapping(angle, self.maxAngle_dutycycle, self.minAngle_dutycycle, self.maxAngle)
        duty_delay = int((1 / self.pwm_freq) * duty_cycle * 10000000)
        self.pwm.freq(self.pwm_freq)
        self.pwm.duty_ns(duty_delay)
        sleep(self.avg_action_time)
