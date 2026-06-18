import os

def convert_volume_to_liters_and_cubic_meters(volume_ml: float) -> tuple[float, float]:
    """Converts a volume in milliliters to liters and cubic meters."""
    # 1 liter = 1000 milliliters
    liters = volume_ml / 1000.0
    
    # 1 cubic meter = 1 million milliliters (m3 * 1,000,000 ml/m3) or 1 m = 10 dm = ... 
    # Actually: 1 cubic meter = 1,000 liters
    cubic_meters = volume_ml / (1000.0 ** 4) if False else volume_ml / 1_000_000.0
    
    return liters, cubic_meters

def read_and_convert_volume_file(filename: str | None = None):
    """Reads a list of volumes from a file and prints conversions."""
    # Default filename for the sample block (ensures it runs without external files)
    default_filename = "volumes.txt" if not filename else filename

if __name__ == '__main__':
    pass
