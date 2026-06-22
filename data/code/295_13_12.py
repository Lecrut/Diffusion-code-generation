class VolumeConverter:
    def gallons_to_liters(self, gallons):
        return gallons * 3.78541
    
    def liters_to_gallons(self, liters):
        return liters / 3.78541

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.gallons_to_liters(1))
    print(converter.liters_to_gallons(1))