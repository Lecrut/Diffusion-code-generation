class VolumeParser:
    DELIMITER = ','
    ERROR_MESSAGE = "Invalid input: All values must be numeric."

    @staticmethod
    def parse_volume_values(volume_string):
        try:
            volume_list = [VolumeParser._parse_float(value.strip()) for value in volume_string.split(VolumeParser.DELIMITER)]
            return volume_list
        except ValueError as e:
            raise ValueError(VolumeParser.ERROR_MESSAGE) from e

    @staticmethod
    def _parse_float(value):
        return float(value)

if __name__ == '__main__':
    sample_input = "3.14, 2.71, 0.98, 1.41"
    try:
        result = VolumeParser.parse_volume_values(sample_input)
        print(result)
    except ValueError as e:
        print(e)