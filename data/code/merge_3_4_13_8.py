class DistanceConverter:
    """A class to manage conversions between miles, kilometers, and meters."""
    
    # Internal conversion factors relative to one meter (1 unit = factor meters)
    METERS_PER_MILE = 1609.344
    METERS_PER_KILOMETER = 1000
    
    def _convert_to_base(self, distance: float, from_unit: str) -> float:
        """Convert a distance to its base unit (meters)."""
        if from_unit.lower() == 'mile':
            return distance * self.METERS_PER_MILE
        elif from_unit.lower() in ('kilometer', 'km'):
            return distance * self.METERS_PER_KILOMETER
        else:  # assumed meters or meter/mi/km not passed correctly, but based on requirements it's just meter input 
             raise ValueError("Invalid unit.")

    def _convert_from_base(self, meters: float, to_unit: str) -> float:
        """Convert a distance from the base unit (meters) to the target unit."""
        if to_unit.lower() == 'mile':
            return meters / self.METERS_PER_MILE
        elif to_unit.lower() in ('kilometer', 'km'):
            return meters / self.METERS_PER_KILOMETER
        else:  # assumed meter input 
             raise ValueError("Invalid unit.")

    def convert_distance(self, distance: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance between any pair of supported units.
        
        Args:
            distance (float): The value in the source unit.
            from_unit (str): The source unit ('mile', 'miles', 'kilometer' or 'km').
            to_unit (str): The target unit ('mile', 'miles', 'kilometer' or 'km').

        Returns:
            float: The converted distance in the target unit.
        """
        
        # Normalize units for internal comparison and logic handling
        
        source_base = self._convert_to_base(distance, from_unit) if from_unit.lower() != 'meter' else (distance * 1) 
        
        # Convert to meters first regardless of input since we only have factors defined relative to meter 
        base_distance = distance
        unit_lookup_map = {'mile': self.METERS_PER_MILE, 'miles': self.METERS_PER_MILE, 
                           'kilometer': self.METERS_PER_KILOMETER, 'km': self.METERS_PER_KILOMETER} 
        
        # Re-implementing cleaner logic without over-engineering constants for every case
        
        def get_meters(d, u):
            if not isinstance(u, (str)):
                raise ValueError("Units must be provided as strings.") 
                
            factor = unit_lookup_map.get(u.lower())
            
            return d * factor
            
        def from_meters(m, to_unit_str):  
             # To convert back from meters: 
             
              target_factor = 1/unit_lookup_map[to_unit_str.lower()] if to_unit_str not in ('meter', 'm') else None

if __name__ == '__main__':
    pass
