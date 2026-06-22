KM_TO_M = 1000

def km_to_meters(kilometers):
    return kilometers * KM_TO_M

if __name__ == '__main__':
    sample_km = 5
    result_m = km_to_meters(sample_km)
    print(f"Input distance in kilometers: {sample_km}")
    print(f"Converted distance in meters: {result_m}")