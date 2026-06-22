class VolumeComparator:
    def compare(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        
        result = None
        if volume1 > volume2:
            result = f"Volume 1 ({volume1}) is greater than Volume 2 ({volume2})."
        elif volume1 < volume2:
            result = f"Volume 1 ({volume1}) is smaller than Volume 2 ({volume2})."
        else:
            result = "Both volumes are equal."
        
        return result

if __name__ == '__main__':
    comparator = VolumeComparator()
    
    vol1 = 75.5
    vol2 = 45.3
    print(comparator.compare(vol1, vol2))
    
    vol3 = 60.0
    vol4 = 60.0
    print(comparator.compare(vol3, vol4))
    
    vol5 = 90.2
    vol6 = 120.8
    print(comparator.compare(vol5, vol6))