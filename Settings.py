import json
import math
import Web
from WeatherType import WeatherType


fileloc = 'json/settings.json'


class Settings(object):
    """Class to hold settings"""

    def __init__(self):
        try:
            self.load_file()
        except IOError:
            print("No settings file found... using defaults")

            self.weather = "normal"  # todo make this the enum
            self.catchup_on = True
            self.catchup_steps = 255
            self.catchup_time = 5
            self.clouds_random_on = False
            self.clouds_random_start_time = 13
            self.clouds_random_end_time = 15
            self.clouds_random_freq = 20
            self.clouds_dim_percent = .20
            self.clouds_dim_resolution = 255
            self.clouds_dim_speed = .05
            self.storms_random_on = True
            self.storms_random_start_time = 21
            self.storms_random_end_time = 0
            self.storms_random_freq = 1000
            self.sound_on = True

            self.dump_file()

    def dump_file(self):
        with open(fileloc, 'w') as data_file:
            string = json.dumps(
                self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            data_file.write(string)

    def load_file(self):
        with open(fileloc) as data_file:
            self.__dict__ = json.load(data_file)

    def web_send(self):
        with open(fileloc) as data_file:
            string = json.dumps(
                self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
            Web.msg(string)

    def web_read(self):
        Web.response()
        
