class VolumeComparator:
    COMPARISON_TEMPLATE = "Volume 1 ({}) is {} than Volume 2 ({})."
    
    def compare(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numbers.")
        
        if volume1 > volume2:
            return self.COMPARISON_TEMPLATE.format(volume1, "greater", volume2)
        elif volume1 < volume2:
            return self.COMPARISON_TEMPLATE.format(volume1, "smaller", volume2)
        else:
            return "Both volumes are equal."

if __name__ == '__main__':
    comparator = VolumeComparator()
    print(comparator.compare(75, 40))
    print(comparator.compare(60, 60))
    print(comparator.compare(90, 120))