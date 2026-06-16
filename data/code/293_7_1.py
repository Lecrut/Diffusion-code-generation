class Measurement:
    def __init__(self, value):
        self._value = value
    def get_value(self):
        return self._value
    def __str__(self):
        return f"{self.__class__.__name__}: {self._value}"
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
    print(mass_obj)
    print(length_obj)
    print(volume_obj)
    print(f"Mass value: {mass_obj.get_value()}")
    print(f"Length value: {length_obj.get_value()}")
    print(f"Volume value: {volume_obj.get_value()}")