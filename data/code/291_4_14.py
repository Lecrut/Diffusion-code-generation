class MeasureComparator:
    YARDS_TO_INCHES = 36

    @staticmethod
    def compare(measure1, unit1, measure2, unit2):
        if unit1 == 'yards':
            measure1 *= MeasureComparator.YARDS_TO_INCHES
        if unit2 == 'yards':
            measure2 *= MeasureComparator.YARDS_TO_INCHES
        if measure1 < measure2:
            return (measure1 / MeasureComparator.YARDS_TO_INCHES, 'yards') if unit1 != 'yards' else (measure1, unit1)
        elif measure2 < measure1:
            return (measure2 / MeasureComparator.YARDS_TO_INCHES, 'yards') if unit2 != 'yards' else (measure2, unit2)
        else:
            return None
if __name__ == '__main__':
    result = MeasureComparator.compare(5, 'yards', 60, 'inches')
    print(result)