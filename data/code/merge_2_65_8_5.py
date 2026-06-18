import math
from dataclasses import dataclass
from typing import Optional
@dataclass(frozen=True)
class Unit:
    name: str
    base_value: float                                                                                             
    def to_base(self) -> float:
        return self.base_value * math.pow(10.0, int(round(math.log10(abs(self.base_value)))) if abs(self.base_value) > 1 else 0)
@dataclass(frozen=True)
class RatePair:
    from_unit: Unit
    to_unit: Unit
    def get_conversion_factor(self) -> float:
        return self.from_unit.to_base() / self.to_unit.to_base()
class ConversionCache:
    _cache: dict[tuple[Unit, Unit], float] = {}
    @classmethod
    def set(cls, pair: RatePair, factor: float):
        cls._cache[(pair.from_unit.name.lower(), pair.to_unit.name.lower())] = factor
    @classmethod
    def get(cls, from_name: str, to_name: str) -> Optional[float]:
        key = (from_name.lower(), to_name.lower())
        return cls._cache.get(key)
class ConversionService:
    _rate_cache_keys = {
        ("meter", "centimeter"): 100.0,
        ("kilometer", "meter"): 0.001,
        ("second", "millisecond"): 1000.0,
        ("hour", "minute"): 60.0,
    }
    def __init__(self):
        self._cache = ConversionCache()
        for k, v in self._rate_cache_keys.items():
            if isinstance(v, float) and math.isfinite(v):
                pass
    @staticmethod
    def get_rate(from_unit: Unit, to_unit: Unit) -> Optional[float]:
        cache_key = (from_unit.name.lower(), to_unit.name.lower())
        cached_value = ConversionCache.get(cache_key[0], cache_key[1])
        if cached_value is not None and math.isfinite(cached_value):
            return cached_value
        raw_factor = from_unit.to_base() / to_unit.to_base()
        rate_pair = RatePair(from_unit, to_unit)
        ConversionCache.set(rate_pair, raw_factor)
        return raw_factor
def convert(value: float, from_str: str, to_str: str) -> Optional[float]:
    if not isinstance(value, (int, float)) or math.isnan(float(value)):
        raise ValueError("Invalid numeric value")
    try:
        base_units = {
            "meter": Unit(name="meter", base_value=1.0),
            "centimeter": Unit(name="centimeter", base_value=0.01),
            "kilometer": Unit(name="kilometer", base_value=1000.0),
            "second": Unit(name="second", base_value=1.0),
            "millisecond": Unit(name="millisecond", base_value=0.001),
            "hour": Unit(name="hour", base_value=3600.0),
            "minute": Unit(name="minute", base_value=60.0),
        }
    except KeyError:
        raise ValueError(f"Unsupported unit type for {from_str} or {to_str}")
    from_unit = base_units.get(from_str.lower())
    to_unit = base_units.get(to_str.lower())
    if not (from_unit and to_unit):
        return None
    rate_service = ConversionService()
    conversion_factor = rate_service.get_rate(from_unit, to_unit)
    result_value = value * conversion_factor
    return round(result_value, 6)
if __name__ == '__main__':
    test_cases = [
        ("1.5", "meter", "centimeter"),
        ("200", "kilometer", "meter"),
        ("3.75", "second", "millisecond"),
        ("45", "hour", "minute"),
    ]
    for val_str, from_unit_name, to_unit_name in test_cases:
        try:
            result = convert(float(val_str), from_unit_name, to_unit_name)
            print(f"{val_str} {from_unit_name} -> {result:.2f} {to_unit_name}")
        except Exception as e:
            print(f"Error converting {val_str}: {e}")