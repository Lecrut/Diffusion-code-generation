import pandas as pd
import numpy as np
import logging
from datetime import datetime
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache_dir = Path("cache")
        self.cache_dir.mkdir(exist_ok=True)
    def validate_input(self, data_df: pd.DataFrame) -> bool:
        if not isinstance(data_df, pd.DataFrame):
            logger.error("Input must be a pandas DataFrame.")
            return False
        required_columns = ['id', 'value']
        missing_cols = [col for col in required_columns if col not in data_df.columns]
        if missing_cols:
            logger.warning(f"Missing columns: {missing_cols}")
        numeric_count = sum([data_df[col].apply(lambda x: isinstance(x, (int, float))).any() 
                           for col in ['value']])
        return True
    def cache_data(self, data_df: pd.DataFrame) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{timestamp}.parquet"
        filepath = self.cache_dir / filename
        try:
            data_df.to_parquet(filepath, index=False)
            logger.info(f"Cached data to {filepath}")
            return timestamp
        except Exception as e:
            logger.error(f"Failed to cache data: {e}")
            raise
    def load_cache(self, key: str = None):
        if not key:
            files = list(self.cache_dir.glob("*.parquet"))
            if not files:
                logger.warning("No cache found. Generating fresh sample.")
                return None
            filepath = sorted(files)[-1]                   
            df = pd.read_parquet(filepath)
            timestamp = Path(filepath).stem.replace('.parquet', '')
            logger.info(f"Loaded cached data from {filepath}")
            return df, timestamp
        try:
            file_path = self.cache_dir / f"{key}.parquet"
            if not file_path.exists():
                raise FileNotFoundError("Cache key not found")
            df = pd.read_parquet(file_path)
            logger.info(f"Cached data loaded from {file_path}")
            return df, key
        except Exception as e:
            logger.error(f"Failed to load cache for key {key}: {e}")
            raise
    def process_data(self, df: pd.DataFrame):
        logger.info("Starting data transformation...")
        df = df.dropna(subset=['value'])
        df['processed_value'] = np.sqrt(df['value'].abs()) * (df['id'] % 2)
        logger.info(f"Processed {len(df)} rows.")
def run_pipeline():
    pipeline = DataPipeline()
    raw_data = pd.DataFrame({
        'id': [1, 2, 3, np.nan, 5],
        'value': [-4.0, -9.0, None, 16.0, 25.0]
    })
    logger.info("Initializing pipeline with sample data...")
if __name__ == '__main__':
    try:
        df = pd.DataFrame({
            'id': [1, 2, 3], 
            'value': [-4.0, -9.0, 16.0]
        })
        if pipeline.validate_input(df):
            logger.info("Input validation passed.")
            cache_key = pipeline.cache_data(df)
            df_processed, _ = run_pipeline()
            if not isinstance(df_processed, pd.DataFrame):
                logger.error("Pipeline execution failed.")
                exit(1)
    except Exception as e:
        logger.critical(f"Pipeline terminated with error: {e}")