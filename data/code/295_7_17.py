def mph_to_kmph(mph):
    conversion_factor = 1.60934
    return f"{mph} mph is {mph * conversion_factor:.2f} km/h"

if __name__ == '__main__':
    sample_mph = 50
    result = mph_to_kmph(sample_mph)
    print(result)