class VolumeComparator:
    def compare(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        
        result = "Both volumes are equal."
        if volume1 > volume2:
            result = f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
        elif volume1 < volume2:
            result = f"Volume 1 ({volume1}) is smaller than Volume 2 ({volume2})."
        
        return result

if __name__ == '__main__':
    comparator = VolumeComparator()
    
    sample_volume_1 = 75.5
    sample_volume_2 = 45.3
    print(comparator.compare(sample_volume_1, sample_volume_2))
    
    sample_volume_3 = 90
    sample_volume_4 = 90
    print(comparator.compare(sample_volume_3, sample_volume_4))
    
    sample_volume_5 = 120
    sample_volume_6 = 80.5
    print(comparator.compare(sample_volume_5, sample_volume_6))