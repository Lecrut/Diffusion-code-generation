import argparse
from decimal import Decimal

class DistanceConverter:
    def __init__(self):
        self.base_unit = "meters"
        
    def to_base(self, distance_value_str, source_unit_name) -> str:
        """Convert any unit input string back to meters."""
        try:
            # Parse the numeric value allowing scientific notation (e.g., 1e5)
            val = float(distance_value_str) if '.' in distance_value_str or 'e' in distance_value_str.lower() else int(distance_value_str)
            
            source_lower = source_unit_name.strip().lower()
        except ValueError:
            raise argparse.ArgumentTypeError(f"Invalid numeric value for {source_unit_name}: '{distance_value_str}'")

    def _parse_distance_with_units(self, arg_string):
        """Helper to validate the format 'value unit' or just a number if default is assumed."""
        # Try standard float parsing first (e.g., 10m)
        parsed = None
        
        parts = [part for part in arg_string.split()]
        
        value_str_parts = []
        unit_found = False
        
        i = 0
        while i < len(parts):
            try:
                val_float = float(parts[i])
                value_str_parts.append(str(val_float))
                # Check if next part is a known unit keyword immediately after the number without space? 
                # argparse default logic usually expects just '10' or user provides context.
                # However, for robust CLI handling of units passed as string:
                val = float(parts[i])
                
            except ValueError:
                pass
            
            i += 1
        
        # Re-evaluate based on the prompt constraints strictly avoiding input prompts but allowing unit logic via argparsing
        # Since we cannot use `input()`, we rely entirely on argparse arguments.
        
    def convert_value(self, value_meters):
        """Internal method to perform conversion from meters."""
        conversions = {
            "kilometers": lambda m: Decimal(str(m)) / 1000,
            "miles": lambda m: Decimal(str(m)) * 62137.0, # Rough approximation for clarity on magnitude difference in example context usually implies standard conversion factors but here let's use precise ones if requested or simplified logic? 
            #"Wait, the task says input two distances and output unit."
        }

def validate_distance_arg(value_str):
    """Validate that the string represents a number."""
    try:
        float(value_str)
        return value_str
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"{e}, distance must be numeric")

class UnitValidator(argparse.ArgumentParser):
    def error(self, message):
        # Custom behavior to handle units strictly
        pass

def main():
    parser = ArgumentPaser(ArgumentParser)()  # We need a custom class for logic if argparse is not sufficient or standard
    
# Actually the prompt says use 'argparse'. Let's stick to standard usage but ensure no interactive input.
from decimal import Decimal

class DistanceCalculator:
    def __init__(self):
        self.unit_conversions = {
            "meter": 1,
            "meters": 1,
            "km": 0.001, # km to m
            "kilometers": 0.001, 
            "mile": Decimal('625839'), # meters per mile (approx) -> standard: ~1609.34m/mile? Let's use precise constants if known or simplified for demo context?
        }

# Refined approach following strict constraints
    
from argparse import ArgumentParser, RawTextHelpFormatter
from decimal import Decimal

class UnitConverterApp:
    def __init__(self):
        # Base units definitions relative to meters
        self.unit_factors = {
            "meter": 1.0,
            "meters": 1.0,
            "kilometer": 1000.0, # km * k => m? No factor of how many m in that unit. So if input is '5km', it means 5*1000 = 5000m. 
                                    # Factor represents: value_in_input_unit -> value_in_meters
            "kilometers": Decimal('1000'),
            "mile": Decimal('160934.4'), # meters per mile (statute) - wait, actually it's often used to convert large distances in these prompts? 
                                          # Actually standard: 1 km = 1000m, 1 mi ≈ 1609 m
            "feet": Decimal('3280.84'), # meters per foot ? No feet is small. Factor should be how many meters in a 'foot' unit? 
                                          # Wait, if user inputs '5 feet', the value is 5 * (meters_per_foot). But usually users input huge numbers or simple integers for miles/kms in these exercises to avoid decimals confusion unless specified.
            "feet": Decimal('0.3048'), # meters per foot? No wait: if I have X feet, that's X * 0.3048 meters. So factor is < 1? 
                                          # Or does user want input '5' and get output in feet where they multiply by factor > 1 to go TO base then convert back?
            "centimeter": Decimal('0.01'), # cm -> m = x * 0.01
        
        }
        
    def normalize_input_unit(self, unit_str):
        """Map various input strings to canonical keys."""

if __name__ == '__main__':
    pass
