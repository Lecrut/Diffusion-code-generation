import argparse
import sys
from typing import Dict, Union

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            "l": 1.0,
            "gal": 0.264172,
            "ml": 1000.0,
            "fl_oz": 33.814,
            "cup": 4.16667,
            "pt": 2.08198,
            "qt": 1.05669,
            "m3": 0.001,
        }

    def convert(self, amount: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unknown input unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unknown output unit: {to_unit}")
        
        base_amount = amount / self.conversion_factors[from_unit]
        return base_amount * self.conversion_factors[to_unit]

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert volume units.")
    parser.add_argument("volume", type=float, help="The volume to convert.")
    parser.add_argument("from_unit", type=str, help="The unit of the input volume.")
    parser.add_argument("to_unit", type=str, help="The desired output unit.")
    
    args = parser.parse_args([])
    
    converter = VolumeConverter()
    result = converter.convert(args.volume, args.from_unit, args.to_unit)
    print(result)

if __name__ == "__main__":
    main()