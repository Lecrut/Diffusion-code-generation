class VolumeAnalyzer:
    COMPARISON_MESSAGES = {
        1: "First volume is greater than the second.",
        -1: "First volume is less than the second.",
        0: "Both volumes are equal."
    }

    @staticmethod
    def compare(volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        return VolumeAnalyzer.COMPARISON_MESSAGES[VolumeAnalyzer._compare_numbers(volume1, volume2)]

    @staticmethod
    def _compare_numbers(a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

if __name__ == '__main__':
    try:
        volume1 = 6.7890
        volume2 = 3.14159
        result = VolumeAnalyzer.compare(volume1, volume2)
        print(result)
    except ValueError as e:
        print(e)