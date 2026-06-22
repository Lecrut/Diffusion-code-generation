class MilesToFeetConverter:
    def __init__(self, miles):
        self.miles = miles

    def to_feet(self):
        return self.miles * 5280

if __name__ == '__main__':
    converter = MilesToFeetConverter(2)
    result = converter.to_feet()
    print(result)