def convert_km_to_miles(km: float) -> float:
    conversion_factor = 0.621371
    return km * conversion_factor

if __name__ == '__main__':
    test_cases = [
        (10.0,),
        (50.0,),
        (1.0,),
        (0.0,)
    ]
    
    for km in test_cases:
        miles = convert_km_to_miles(km[0])
        print(f"{km[0]} km is {miles:.2f} miles")