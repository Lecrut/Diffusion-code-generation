import time
import math
from typing import List, Tuple

def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate area of a single rectangle."""
    return width * height

def calculate_circle_area(radius: float) -> float:
    """Calculate area of a single circle."""
    return math.pi * (radius ** 2)

class PerformanceBenchmark:
    def __init__(self, iterations: int):
        self.iterations = iterations
        
    def benchmark_rectangle(self, widths: List[float], heights: List[float]) -> float:
        """Measure performance of calculating areas for rectangles."""
        total_widths = sum(widths)
        total_heights = sum(heights)
        
        start_time = time.perf_counter()
        
        # Pre-calculate dimensions to ensure consistent data generation if needed,
        # though here we just use the provided lists.
        results_rectangles = [calculate_rectangle_area(w, h) for w in widths for h in heights]
        
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        
        return elapsed_time

    def benchmark_circle(self, radii: List[float]) -> float:
        """Measure performance of calculating areas for circles."""
        results_circles = [calculate_circle_area(r) for r in radii]
        
        # Calculate total time by summing individual times is not feasible here as we need a bulk run.
        # We'll re-run the list comprehension directly to measure total elapsed time accurately.
        start_time = time.perf_counter()
        results_circles_final = [calculate_circle_area(r) for r in radii]
        
        end_time = time.perf_counter()
        
        return end_time - start_time

class RectangleGenerator:
    def __init__(self, count: int):
        self.count = count
        
    def generate(self) -> Tuple[List[float], List[float]]:
        """Generate random dimensions for rectangles."""
        widths = [math.random() * 10.0 + 0.5 for _ in range(int(math.sqrt(self.count)))]
        heights = [math.random() * 10.0 + 0.5 for _ in range(int(math.sqrt(self.count)))]
        
        # Repeat generation to fill the list if needed, but simply flattening is not required 
        # as we can generate pairs directly or assume a grid-like distribution logic implicitly handled by comprehension.
        # To strictly match '10,000 rectangles', we need 50x2 rows or similar structure effectively yielding N items.
        
        # Let's create two lists of size M such that M*M >= count for simplicity in pairing if needed, 
        # but simpler is to just generate a flat list logic where each rectangle takes one iteration step?
        # Actually, the benchmark loop usually iterates once per shape or twice (once w, once h).
        # To keep it simple and efficient: Generate 100 widths and 100 heights -> 10,000 rects.
        
        return list(widths), list(heights)

class CircleGenerator:
    def __init__(self, count: int):
        self.count = count
        
    def generate(self) -> List[float]:
        """Generate random radii for circles."""
        # Generate sqrt(count) items? No, just one radius per rectangle iteration logic if we were pairing.
        # Here we need 10,000 circles total. So generate list of size count or larger chunks.
        
        return [math.random() * 5 + 0.1 for _ in range(self.count)]

def main():
    N = 10000
    
    rect_gen = RectangleGenerator(N)
    circle_gen = CircleGenerator(N)
    
    widths, heights = rect_gen.generate()
    radii = circle_gen.generate()
    
    # Ensure we have enough items. 
    # The comprehension [calc(w,h) for w in widths for h in heights] creates N rectangles if len(widths)*len(heights)==N.
    # So let's adjust width/height count to be sqrt(N).
    num_per_dim = int(math.sqrt(N))
    
    rect_gen_adjusted = RectangleGenerator(num_per_dim * num_per_dim)
    circle_gen_adjusted = CircleGenerator(num_per_dim * num_per_dim)
    
    widths, heights = [0.5 + i*0.1 for i in range(num_per_dim)], [0.5 + j*0.1 for j in range(num_per_dim)] # Deterministic sample for reproducibility without input() logic issues but using fixed values per requirement? 
    # Wait, "hard-coded sample values" implies constant inputs or random with seed?
    # The prompt says: "Include an if __name__ == '__main__': block with hard-coded sample values."
    # It also forbids interactive prompts. Using a list literal is safest as it doesn't rely on external state or randomness unless seeded, 
    # but calculating area performance usually benefits from varied data to avoid micro-optimizations hiding real algospeed differences if any (though here both are O(1)).
    
    # Let's use fixed lists for determinism and safety.
    sample_widths = [i * 0.5 + 2.0 for i in range(num_per_dim)]
    sample_heights = [j * 0.6 - 3.0 for j in range(num_per_dim) if abs(j*0.6-3.0)>0] # ensure positive height roughly
    
    # Recalculate to be simple and safe: just fill exactly num_per_dim x num_per_dim
    sample_widths = [float(i + 1) * 2.5 for i in range(num_per_dim)] 
    sample_heights = [float(j + 3) / 4.0 for j in range(num_per_dim)]

    # Re-generate radii deterministically based on index to avoid 'input' style randomness dependency
    # Actually, standard random module works fine without input prompt as long as no stdin is called.
    # But let's stick to explicit hard-coded lists or a seeded generator if needed? 
    # Python 3's random with default seed is technically non-deterministic across runs unless set.seed() is used.
    # To be safe and strictly "hard coded sample values", we can precompute the list contents inside main().
    
    final_radii = [math.pi * (k + 0.5) ** 2 for k in range(num_per_dim)] # Just using area directly? No, need radius input to test algorithm.
    # Let's do: radii values are constants computed here.
    
    sample_radii_values = []
    current_val = math.pi * (10**5) / 14 
    for _ in range(num_per_dim):
        sample_radii_values.append(current_val + (_ - num_per_dim//2)*0.1)

    # Actually, let's just use simple integers or floats defined directly to ensure no external imports beyond math/time are needed if possible? No, time and math are standard lib.
    
    # Let's redefine the sample generation block for clarity:
    # We will create lists explicitly with fixed values to satisfy "hard-coded sample values".
    
    num_items_per_side = 100 
    total_rectangles = num_items_per_side * num_items_per_side
    
    widths_list = [float(i + 2) for i in range(num_items_per_side)]
    heights_list = [float(j + 3.5) / 8.0 for j in range(num_items_per_side)] # Ensure positive height > width logic? No, just valid dimensions.