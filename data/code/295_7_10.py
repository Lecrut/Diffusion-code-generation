def mph_to_kmh(mph):
    return mph * 1.60934

if __name__ == '__main__':
    sample_mph = 50
    kmh = mph_to_kmh(sample_mph)
    print(f"{sample_mph} mph is {kmh:.2f} km/h")