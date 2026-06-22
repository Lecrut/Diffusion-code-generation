def mph_to_kmh(mph):
    conversion_factor = 1.60934
    kmh = mph * conversion_factor
    return f"{mph} mph is {kmh:.2f} km/h"

if __name__ == '__main__':
    sample_mph = 50
    print(mph_to_kmh(sample_mph))