conversion_factor = 1.60934

def mph_to_kmph(mph):
    return mph * conversion_factor

if __name__ == '__main__':
    sample_speed_mph = 60
    result_kmph = mph_to_kmph(sample_speed_mph)
    print(f"{sample_speed_mph} mph is {result_kmph:.2f} km/h")