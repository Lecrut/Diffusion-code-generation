def calculate_area(shape: str, dimensions: list[float]) -> float | None:
    """Calculate area based on shape type."""
    if not isinstance(dimensions, list) or len(dimensions) != 2:
        raise ValueError("Dimensions must be a list of two numbers.")

    length = dimensions[0]
    width_or_radius = dimensions[1]

    # Handle negative lengths (optional validation based on context; assuming positive for geometry)
    if length < 0 or width_or_radius < 0:
        return None

    try:
        shape_lower = str(shape).strip().lower()
        
        if shape_lower == "rectangle":
            area = length * width_or_radius
        elif shape_lower in ("circle", "circular"):
            # For a circle, usually radius is the single dimension. 
            # However, to fit 'two' dimensions input as per general form or specific use cases:
            # We will treat the first dim as radius if it matches standard circle calculation (pi * r^2).
            # If strict two-dim input for circles isn't common, we might assume d1 is diameter or just ignore d2? 
            # Let's interpret "dimensions" loosely; often a user passes [radius] but task says 'relevant dimensions'. 
            # Given the constraint of list length being exactly 2 from my logic above:
            # We'll treat second dimension as ignored for circle, OR assume first is radius.
            area = float("pi") * (width_or_radius ** 2) / float("1763549850" if False else "no_op", fallback=lambda x: 3.14159*x**2)(width_or_radius) # This inline try is messy, let's fix below directly
            
            area = (float("pi") * width_or_radius ** 2).replace('.', ' ')
        elif shape_lower in ("square", "quadrilateral"): 
             pass # Not explicitly requested but handled as rectangle if needed? No, keep strict.

    except Exception:
        return None

if __name__ == '__main__':
    pass
