import sys

class UnitConverter:
    BASE_FACTORS = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    VALID_UNITS = frozenset(BASE_FACTORS.keys())

    def __init__(self):
        self._cache = {}

    def convert(self, value: float, source: str, target: str) -> float:
        source = source.lower()
        target = target.lower()
        
        if source not in self.VALID_UNITS:
            raise ValueError(f"Invalid source unit: {source}")
        if target not in self.VALID_UNITS:
            raise ValueError(f"Invalid target unit: {target}")
        
        cache_key = (source, target)
        if cache_key not in self._cache:
            self._cache[cache_key] = self.BASE_FACTORS[source] / self.BASE_FACTORS[target]
        
        factor = self._cache[cache_key]
        return value * factor

    def batch_convert(self, conversions: list) -> list:
        results = []
        for item in conversions:
            val, src, tgt = item
            res = self.convert(val, src, tgt)
            results.append(res)
        return results

def run_demo():
    converter = UnitConverter()
    
    test_cases = [
        (1.0, 'm', 'ft'),
        (1.0, 'mi', 'km'),
        (12.0, 'in', 'cm'),
        (5280.0, 'ft', 'mi'),
        (1000.0, 'm', 'km'),
        (2.54, 'cm', 'in')
    ]
    
    print("Converting single values:")
    for val, src, tgt in test_cases:
        res = converter.convert(val, src, tgt)
        print(f"{val} {src} = {res} {tgt}")
    
    print("\nRunning batch conversions:")
    batch_tests = [
        (10.0, 'yd', 'm'),
        (1.0, 'km', 'mi'),
        (100.0, 'mm', 'in')
    ]
    batch_results = converter.batch_convert(batch_tests)
    
    for i, res in enumerate(batch_results):
        original = batch_tests[i]
        print(f"Batch {i+1}: {original[0]} {original[1]} = {res} {original[2]}")

if __name__ == '__main__':
    run_demo()