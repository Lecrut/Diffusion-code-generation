class NanometerConverter:
    def nm_to_m(self, nanometers):
        return nanometers * 1e-9

if __name__ == '__main__':
    converter = NanometerConverter()
    nm_values = [1000, 5000, 10000]
    for nm in nm_values:
        m = converter.nm_to_m(nm)
        print(f"{nm} nanometers is equal to {m:.9f} meters")