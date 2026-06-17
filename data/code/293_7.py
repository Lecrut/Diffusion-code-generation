class Measurement:
    def __init__(self, value):
        self._value = value
    def get_value(self):
        return self._value
class Mass(Measurement):
    def __init__(self, value):
        super().__init__(value)
class Length(Measurement):
    def __init__(self, value):
        super().__init__(value)
class Volume(Measurement):
    def __init__(self, value):
        super().__init__(value)
if __name__ == '__main__':
    mass_obj = Mass(10.5)
    length_obj = Length(2.5)
    volume_obj = Volume(5.0)
    print(f"Mass: {mass_obj.get_value()}")
    print(f"Length: {length_obj.get_value()}")
    print(f"Volume: {volume_obj.get_value()}")