class YardConverter:
    def __init__(self):
        self.conversion_factor = 0.9144

    def yards_to_meters(self, yards):
        return [round(y * self.conversion_factor, 3) for y in yards]

if __name__ == '__main__':
    converter = YardConverter()
    sample_yards = [10, 20, 30]
    print(converter.yards_to_meters(sample_yards))