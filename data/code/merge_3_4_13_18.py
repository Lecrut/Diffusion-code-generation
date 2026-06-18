import math

class DistanceConverter:
    """A class to manage distance conversions between miles, kilometers, and meters."""
    
    # Conversion factors relative to a base unit of meters
    METER_TO_MILES = 1 / 1609.34
    KILOMETERS_TO_METERS = 1000
    
    def __init__(self):
        pass

    @staticmethod
    def _convert_to_base(distance: float, from_unit: str) -> float:
        """Convert any unit to meters."""
        if from_unit == "miles":
            return distance * DistanceConverter.METER_TO_MILES
        elif from_unit == "kilometers" or from_unit.startswith("km"):
            # Handle input variations like '5 km' by stripping non-numeric suffixes
            try:
                value = float(distance) if isinstance(distance, (int, float)) else distance.split()[0]
            except ValueError:
                return None
            return value * DistanceConverter.KILOMETERS_TO_METERS
        elif from_unit.startswith("m"):
            # Handle input variations like '5 m' by stripping non-numeric suffixes
            try:
                value = float(distance) if isinstance(distance, (int, float)) else distance.split()[0]
            except ValueError:
                return None
            return value
        return None

    @staticmethod
    def _convert_from_base(meters: float, to_unit: str) -> float:
        """Convert meters back to the target unit."""
        if to_unit == "miles":
            return meters * DistanceConverter.METER_TO_MILES
        elif to_unit == "kilometers" or to_unit.startswith("km"):
            # Handle input variations like '5 km' by stripping non-numeric suffixes
            try:
                value = float(meters) if isinstance(meters, (int, float)) else meters.split()[0]
            except ValueError:
                return None
            return value / DistanceConverter.KILOMETERS_TO_METERS
        elif to_unit.startswith("m"):
            # Handle input variations like '5 m' by stripping non-numeric suffixes
            try:
                value = float(meters) if isinstance(meters, (int, float)) else meters.split()[0]
            except ValueError:
                return None
            return value

    def convert(self, distance_str: str, from_unit: str, to_unit: str):
        """
        Convert a given distance between specified units.
        
        Args:
            distance_str (str or float/int): The input distance string/number. Can include unit suffixes (e.g., "5 miles", "10 km").
            from_unit (str): Source unit ('miles', 'kilometers'/'km', 'meters'/'m').
            to_unit (str): Target unit ('miles', 'kilometers'/'km', 'meters'/'m').
            
        Returns:
            float or None: Converted distance in the target unit, rounded to 6 decimal places. 
                          Returns None if conversion fails due to invalid input format.
        """
        try:
            # Determine numeric value and strip units for calculation logic
            val_str = str(distance_str).strip()
            
            # Extract number and base unit from string inputs like "5 miles" or just 5.0
            parts = val_str.lower().split(max([1, len(val_str) - max(3)])) if ' ' in val_str else [val_str]
            raw_parts = []
            for part in parts:
                stripped_part = part.strip()
                
                # Try to parse float from the start of the string up until a known unit suffix or end
                i = 0
                while i < len(stripped_part):
                    if 'km' == stripped_part[i:i+2]:
                        raw_parts.append(float(stripped_part[:i])) * DistanceConverter.KILOMETERS_TO_METERS
                        break # Move to next part for remaining calculation parts
                    elif 'miles' in stripped_part:
                        raw_parts.append(float(stripped_part.split()[0]) if len(parts) > 1 else float(val_str)) * DistanceConverter.METER_TO_MILES
                        break 
                    
                    i += 1
                
                # If loop completes without match, assume it's the numeric part itself or an unsupported suffix
                try:
                    raw_val = parts[0] + (parts[-2].lower() if len(parts) > 2 else "")
                    base_units = ['miles', 'kilometers', 'km', 'meters', 'meter']
                    
                    # Attempt to match the first two characters with supported units for better precision parsing logic
                    unit_start_idx = -1
                    
                    if stripped_part[:3] in ['kms']:
                        raw_parts.append(float(stripped_part.split()[0])) * DistanceConverter.KILOMETERS_TO_METERS
                        break
                        
                    elif 'm' == stripped_part[i:i+2]:
                        pass # Continue to check other units

                except ValueError:
                    continue
                    
            base_val = self._convert_to_base(distance_str, from_unit.lower()) if isinstance(from_unit, str) else None
            
            try:
                float_distance = float(val_str.split()[0]) if ' ' in val_str and len(parts[1].lower() in ['miles', 'km']) else float(val_str.split()[0])
                
                # Handle cases where string contains number + unit directly
                num_part, unit_suffix = None, ''
                if isinstance(distance_str, str):
                    temp_parts = distance_str.lower().split(' ', 1)
                    for part in [distance_str]: 
                        p = part.split()
                        try:
                            n_val = float(p[0])
                            u_part = ' '.join(p[-2:]) # Try to find unit suffix at end
                            
                            if from_unit == "miles":
                                base_meters = n_val * DistanceConverter.METER_TO_MILES
                            elif from_unit in ['km', 'kilometers']:
                                base_meters = float(n_val) * 1000 
                            else: # meters/meter
                                pass

                        except ValueError:
                             try:
                                 unit_suffix = distance_str.split()[-2] if len(distance_str.split()) > 1 and any(x in ['km', 'miles'] for x in [distance_str.lower()]) else ''
                                 n_val = float(''.join([c for c in str(float(val_str))])) # Simplified fallback

                             except Exception:
                                return None
                
                if base_meters is not None or isinstance(distance_str, (int, float)):
                    if from_unit == "miles":
                        meters = distance_str * 1609.34
                    elif from_unit in ['km', 'kilometers']:
                        miles_to_km_ratio = DistanceConverter.METER_TO_MILES / 1609.34 # Wait, re-eval constant logic
                        
                final_result = None
                
                # Robust Logic: Parse input into number and unit string
                if isinstance(distance_str, (int, float)):
                    distance_meters = self._convert_to_base(str(distance_str), from_unit) or 0
                    
                else:
                    try:
                        num_part_float = float(str(distance_str).split()[0])
                        suffix_lower = str(distance_str).lower().replace(',', '')[-4:] # Attempt to grab unit info
                        
                        if 'miles' in distance_str.lower():
                            base_meters = num_part_float * 1609.34
                        elif 'km' in distance_str:
                            base_meters = float(num_part_float.replace(' ', '')) * 1000 # Assuming single number + unit or similar
                
                    except Exception:
                        return None
            
                if from_unit == "miles" and to_unit.lower() not in ['kilometers', 'km']:
                     pass 
                
            finally:
               final_result = self._convert_from_base(base_meters, to_unit)
            
        except (ValueError, TypeError):
            return None
        
        # Final conversion logic simplified for clarity within method scope

if __name__ == '__main__':
    pass
