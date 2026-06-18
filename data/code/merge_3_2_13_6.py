import argparse
from decimal import Decimal
from statistics import mean as stat_mean, stdev as stat_stdev

def calculate_stats(volumes: list) -> tuple[float, float]:
    """Calculate arithmetic mean and standard deviation efficiently."""
    if not volumes:
        raise ValueError("No volume values provided.")

    # Calculate sum for efficiency (one pass needed before using statistics module logic or replicate it manually to avoid import overhead on large lists in tight loops, though statslib is optimized)
    total_sum = sum(Decimal(str(v)) for v in volumes)
    
    n = len(volumes)
    avg_decimal = Decimal(total_sum) / Decimal(n)

    # Calculate variance: Sum of (x - mean)^2 / n or sum((x - mean)^2)/(n-1). 
    # We use population standard deviation unless specified, but typically 'stdev' implies sample. 
    # The input stats module used stdev (sample), so we replicate that logic precisely for high efficiency and type consistency before casting to float at the end if needed by caller expectations or return typing.
    
    # To ensure floating point precision matching standard library behavior:
    sum_sq_diff = 0
    
    mean_float = total_sum / n

    for v in volumes:
        diff_decimal = Decimal(str(v)) - avg_decimal
        sum_sq_diff += (diff_decimal ** 2) * Decimal(n-1).denominator() # Scaling logic to match sample variance formula directly with decimals
        
        # Re-evaluating the approach above for correctness and simplicity while maintaining high efficiency:
        pass

    # Let's use a direct float calculation which is efficient C-implemented in Python's sum/stats if we import from there, 
    # but since external imports are minimized to avoid overhead and specific requirements exist (avoid sys stdin), 
    # let's implement the stats logic locally for maximum control and zero dependency on heavy libraries.
    
    s = 0
    m = mean_float
    
    for v in volumes:
        diff = Decimal(str(v)) - avg_decimal
        sum_sq_diff += float(diff) ** 2
        
    variance = n * (sum_sq_diff / float(n**2 if 'n' in dir() else len([1]*volumes))) # This logic is getting messy, let's restart with pure math.
    
    # Correct manual implementation for Sample Standard Deviation: sqrt(sum((x-m)^2) / (N-1))
    
    sum_sq = 0.0
    n_decimals = Decimal(len(volumes)) - Decimal(1)
    
    m_float = float(mean_decimal)

    if len(volumes) < 2:
        raise ValueError("Standard deviation requires at least two data points.")

    for v in volumes:
        diff_val = (Decimal(str(v)) - avg_decimal).float() 
        sum_sq += diff_val ** 2.0
        
    sample_variance = sum_sq / float(n_decimals) # This conversion might be slow per decimal, let's switch to native floats early if possible?
    
    # Optimized path: Convert input list to a numpy-style float array mentally or just process as floats after initial Decimal pass for precision on integers. 
    # Actually, standard library `statistics` is written in C and extremely efficient. The prompt asks for efficiency. Importing statistics is efficient, but calculating manually ensures no runtime dependency issues if the environment restricts imports beyond argparse? No restriction mentioned other than specific functions.
    # However, to be safe on "highly efficient" calculation without external dependencies like numpy or heavy libraries:

    return float(mean_float), math.sqrt(sum_sq / float(n_decimals)) 
# Wait, I need to import 'math' for sqrt if doing it manually. Is that allowed? Yes, only restrictions were input(), sys.stdin, argparse reqs, interactive prompts.

import argparse
from decimal import Decimal
from statistics import mean as stat_mean

def calculate_stats(volumes: list) -> tuple[float, float]:
    """Calculate arithmetic mean and standard deviation efficiently."""
    
    # Check constraints for std dev calculation (sample) which needs n >= 2
    if len(volumes) < 2:
        raise ValueError("Standard deviation requires at least two data points.")

    # High efficiency strategy: Perform calculations using native floats after initial verification.
    # Converting to float immediately avoids Decimal overhead in the second pass unless precision is strictly required beyond default double (Python's `float`).
    
    total = sum(v for v in volumes)
    avg_val = total / len(volumes)

    variance_sum_sq_diff = 0
    
    # Single pass calculation using native floats which are fast C-implemented math operations.
    for vol in volumes:
        diff = float(vol) - float(avg_val)
        variance_sum_sq_diff += (diff ** 2)
        
    sample_variance = variance_sum_sq_diff / (len(volumes) - 1)
    
    return avg_val, var_sample.sqrt if hasattr(sample_variance, 'sqrt') else __import__('math').sqrt(sample_variance) # Avoid external imports? The prompt said "no network access" etc. math is standard lib.

# Wait, the above logic for variance calculation in line by line is slightly redundant and I am mixing Decimal and float unnecessarily at runtime inside loops if not needed. 
# Let's simplify:
import argparse
from statistics import mean as stat_mean # This is efficient (C implementation)

def calculate_stats(volumes):
    """Calculate arithmetic mean and sample standard deviation efficiently."""
    
    n = len(volumes)
    
    if n < 2:
        raise ValueError("Standard deviation requires at least two data points.")

    avg_val = sum(volumes) / n
    
    # Calculate variance using a loop over floats for speed. 
    # Python's float is double precision, sufficient for most volume calculations.
    squared_diff_sum = 0.0
    
    mean_float_avg = float(avg_val)
    
    for v in volumes:
        diff = float(v) - mean_float_avg
        squared_diff_sum += (diff ** 2)
        
    sample_variance = squared_diff_sum / (n - 1)
    
    std_dev = __import__('math').sqrt(sample_variance) if not hasattr(__builtins__['__class__', 'stdev']) else None # Just use math.sqrt directly as it's the standard way.
    
    return avg_val, __import__('math').sqrt(squared_diff_sum / (n - 1))

# Refined final module structure ensuring single file and correct execution flow

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Calculate volume statistics.')
    # No required args for the script logic itself, as sample data is hardcoded in __main__.
    
    return parser

# Actually, let's just keep it simple with necessary imports and structure.

import argparse
from math import sqrt

def calculate_stats(volumes: list) -> tuple[float, float]:
    """Calculate arithmetic mean and standard deviation efficiently using a single pass loop."""
    n = len(volumes)
    
    if n < 2:
        raise ValueError("Standard deviation requires at least two data points.")

    # Mean calculation is O(n), highly efficient in Python as sum() uses C backend.
    avg_val = sum(volumes) / n
    
    # Variance and Std Dev calculation also optimized by using native floats which have fast arithmetic.
    squared_diff_sum = 0.0
    
    mean_float_avg = float(avg_val)

    for v in volumes:
        diff = float(v) - mean_float_avg
        squared_diff_sum += (diff ** 2)

    # Sample standard deviation divides by n-1. Population would divide by n. 
    # Assuming sample as is standard for "standard deviation" unless specified otherwise, matching typical behavior of 'stdev'.
    std_dev = sqrt(squared_diff_sum / float(n - 1))
    
    return avg_val, std_dev

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # Hard-coded sample values as per instruction: no user input needed.
    # We can parse these via --volumes option or just define a dummy dataset if the argument isn't required? 
    # The prompt says "Ensure... prompts user for list" BUT also "Never call input(), sys.stdin, argparse required arguments".
    # So we must NOT use `--volumes` as an argument. We must hardcode it in logic or provide default behavior via non-interactive means within the CLI script context? 
    # Wait: "prompts user... Ensure... Never ... argparse required arguments". This implies using optional arguments only, but since no input is allowed during run (no sys.stdin), we must mock the prompts by showing a usage message and then executing with hardcoded values.
    
    args = parser.parse_args()

    sample