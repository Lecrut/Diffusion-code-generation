class VolumeCalculator:
    MIN_VOLUMES = 1

    @staticmethod
    def calculate_average_volume(volumes):
        if len(volumes) < VolumeCalculator.MIN_VOLUMES:
            raise ValueError("The list of volumes cannot be empty.")
        return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [25, 75, 125, 175, 225]
    try:
        average_volume = VolumeCalculator.calculate_average_volume(sample_volumes)
        print(average_volume)
    except ValueError as e:
        print(e)