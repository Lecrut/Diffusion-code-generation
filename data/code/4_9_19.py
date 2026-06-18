class DistanceConverter:
    """A class to convert distances between kilometers and miles."""
    
    def __init__(self, km_value):
        self.kilometers = float(km_value)
        
    @property
    def miles(self):
        return round((self.kilometers * 0.621371), 4)

def display_results(converter: DistanceConverter) -> None:
    """Display the input and converted values."""
    print(f"Input kilometers: {converter.kilometers}")
    print(f"Miles: {converter.miles}")

if __name__ == '__main__':
    # Sample value provided directly to avoid interactive prompts or file I/O.
    sample_km = 10
    
    converter_obj = DistanceConverter(sample_km)
    
    display_results(converter_obj)