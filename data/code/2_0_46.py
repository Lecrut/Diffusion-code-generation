class VolumeCalculator:
    MIN_VOLUME = 1

    @staticmethod
    def validate_volumes(volumes):
        if not volumes:
            raise ValueError("The list of volumes cannot be empty.")
        for volume in volumes:
            if volume < VolumeCalculator.MIN_VOLUME:
                raise ValueError(f"Volume {volume} is below the minimum allowed volume of {VolumeCalculator.MIN_VOLUME}.")

    @staticmethod
    def calculate_average_volume(volumes):
        VolumeCalculator.validate_volumes(volumes)
        return sum(volumes) / len(volumes)

if __name__ == '__main__':
    sample_volumes = [25, 35, 45, 55, 65]
    average_volume = VolumeCalculator.calculate_average_volume(sample_volumes)
    print(average_volume)