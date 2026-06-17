from dataclasses import dataclass
@dataclass(frozen=True)
class Gallon:
    value: float
@dataclass(frozen=True)
class Quart:
    value: float
@dataclass(frozen=True)
class Pint:
    value: float
@dataclass(frozen=True)
class Cup:
    value: float
@dataclass(frozen=True)
class FluidOunce:
    value: float
@dataclass(frozen=True)
class Liter:
    value: float
@dataclass(frozen=True)
class Milliliter:
    value: float
def gallons_to_quarts(gallons: Gallon) -> Quart:
    return Quart(value=gallons.value * 4.0)
def quarts_to_pints(quarts: Quart) -> Pint:
    return Pint(value=quarts.value * 2.0)
def pints_to_cups(pints: Pint) -> Cup:
    return Cup(value=pints.value * 2.0)
def cups_to_fluid_ounces(cups: Cup) -> FluidOunce:
    return FluidOunce(value=cups.value * 8.0)
def fluid_ounces_to_gallons(fluid_ounces: FluidOunce) -> Gallon:
    return Gallon(value=fluid_ounces.value / (128.0))
def liters_to_milliliters(liters: Liter) -> Milliliter:
    return Milliliter(value=liters.value * 1000.0)
def milliliters_to_liters(milliliters: Milliliter) -> Liter:
    return Liter(value=milliliters.value / 1000.0)
def gallons_to_liters(gallons: Gallon) -> Liter:
    return Liter(value=gallons.value * 3.785411784)
def liters_to_gallons(liters: Liter) -> Gallon:
    return Gallon(value=liters.value / 3.785411784)
if __name__ == '__main__':
    sample_input = Gallon(2.0)
    result_quarts = gallons_to_quarts(sample_input)
    print(f"{sample_input} -> {result_quarts}")
    intermediate_pints = quarts_to_pints(result_quarts)
    final_cups = pints_to_cups(intermediate_pints)
    print(f"Intermediate: {intermediate_pints}, Final Cups: {final_cups}")
    converted_back_gallons = fluid_ounces_to_gallons(FluidOunce(value=256.0))
    print(f"{converted_back_gallons} gallons")
    metric_conversion = liters_to_milliliters(Liter(1.0))
    print(f"Metric: {metric_conversion}")
    reverse_metric = milliliters_to_liters(Milliliter(value=3785.411784))
    print(f"Reverse Metric: {reverse_metric} -> {gallons_to_liters(reverse_metric)}")