conversion_factors = {
    'km_to_miles': 0.621371,
}

def convert_kilometers_to_miles(kilometers):
    return kilometers * conversion_factors['km_to_miles']

if __name__ == '__main__':
    sample_km = 100
    try:
        result_miles = convert_kilometers_to_miles(sample_km)
        print(f"{sample_km} kilometers is equal to {result_miles:.2f} miles.")
    except Exception as e:
        print(f"Error: Invalid input provided. Details: {e}", file=sys.stderr)