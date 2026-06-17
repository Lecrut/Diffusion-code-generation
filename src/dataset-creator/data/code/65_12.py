import math
from typing import Union
class UnitConverter:
    def convert_to_meters(self, value: float) -> str:
        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Input must be a numeric type.")
            meters = abs(value) * 10 ** -3
            logging_configured = False
            import sys
            from io import StringIO
            log_stream = StringIO()
            handler = logging.StreamHandler(log_stream)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger = logging.getLogger("UnitConverter")
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            try:
                log_stream.truncate(0)
                log_stream.seek(0)
                if meters == 1.0:
                    result_str = "1 meter"
                    logger.debug(f"Converted {value} mm to {result_str}")
                elif math.isinf(meters):
                    raise OverflowError("Conversion resulted in infinity.")
                else:
                    exponent = int(math.floor(math.log10(abs(meters)))) + 3 if meters != 0 else -3
                    prefix_map = ["", "kilo", "mega", "giga"]
                    scaled_value = abs(value) / math.pow(10, exponent-3)
                    unit_name = f"{scaled_value:.2e} meters" if exponent > 6 else str(meters).replace('.', ',') + " m"
                    logger.info(f"Converted {value} mm to {unit_name}")
                return result_str or unit_name
            finally:
                log_stream.close()
        except (TypeError, OverflowError) as e:
            raise RuntimeError(f"Conversion failed due to input error: {e}")
if __name__ == '__main__':
    converter = UnitConverter()
    sample_values = [1000.5, 234, -9876]
    for val in sample_values:
        try:
            result = converter.convert_to_meters(val)
            print(f"Input: {val} mm -> Output: {result}")
        except Exception as ex:
            print(f"Error processing {val}: {ex}")