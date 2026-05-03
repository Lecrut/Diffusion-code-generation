import typing
class VolumeConverter:
    @staticmethod
    def metric_to_imperial_liters(volume_liters: float) -> float:
        return volume_liters * 0.264172
    @staticmethod
    def metric_to_imperial_gallons(volume_liters: float) -> float:
        return volume_liters * 0.264172
    @staticmethod
    def imperial_to_metric_liters(volume_gallons: float) -> float:
        return volume_gallons / 0.264172
    @staticmethod
    def imperial_to_metric_gallons(volume_gallons: float) -> float:
        return volume_gallons
if __name__ == '__main__':
    print("--- Metric to Imperial Conversions ---")
    metric_volume_ml = 500.0
    metric_volume_m3 = 1.5
    liters_from_ml = metric_volume_ml / 1000.0
    gallons_from_ml = VolumeConverter.metric_to_imperial_gallons(liters_from_ml)
    print(f"Metric: {metric_volume_ml} mL")
    print(f"Converted to Liters: {liters_from_ml:.4f} L")
    print(f"Converted to Gallons: {gallons_from_ml:.4f} gal")
    print("\n--- Imperial to Metric Conversions ---")
    imperial_volume_gal = 10.0
    liters_from_gal = VolumeConverter.imperial_to_metric_liters(imperial_volume_gal)
    print(f"Imperial: {imperial_volume_gal} gal")
    print(f"Converted to Liters: {liters_from_gal:.4f} L")