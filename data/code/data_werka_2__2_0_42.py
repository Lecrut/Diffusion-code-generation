class VolumeCalculator:
    EMPTY_LIST_ERROR = "The list of volumes cannot be empty."

    @staticmethod
    def calculate_average_volume(volumes):
        if not volumes:
            raise ValueError(VolumeCalculator.EMPTY_LIST_ERROR)
        return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [25, 75, 100, 150, 200]
    try:
        average_volume = VolumeCalculator.calculate_average_volume(sample_volumes)
        print(average_volume)
    except ValueError as e:
        print(e)