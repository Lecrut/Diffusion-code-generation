class Conversion:
    FACTOR = 12

    @staticmethod
    def feet_to_inches(feet: int) -> int:
        return feet * Conversion.FACTOR

if __name__ == '__main__':
    feet_input = 10
    inches_output = Conversion.feet_to_inches(feet_input)
    print(inches_output)