import pandas as pd
import numpy as np
import logging
from datetime import datetime
from pathlib import Path
import pickle
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline_debug.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
class DataPipeline:
    def __init__(self):
        self.cache_dir = Path("cache")
        self.cache_dir.mkdir(exist_ok=True)
    def validate_data(self, df: pd.DataFrame) -> bool:
        logger.info(f"Starting validation for shape {df.shape}")
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        required_columns = ['id', 'value']
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            return False
        null_count = df.isnull().sum()
        total_nulls = null_count.sum()
        if total_nulls > 0:
            logger.warning(f"Found {total_nulls} null values in the dataset")
        numeric_dtypes = [col for col, dtype in df.dtypes.items() if np.issubdtype(dtype, np.number)]
        min_max_issues = []
        for col in numeric_dtypes:
            try:
                col_min = df[col].min()
                col_max = df[col].max()
                if not pd.isna(col_min):
                    logger.info(f"Validated column '{col}': min={col_min}, max={col_max}")
            except Exception as e:
                logger.error(f"Error validating numeric range in {col}: {e}")
        return True
    def load_from_cache(self, filename: str) -> pd.DataFrame | None:
        cached_file = self.cache_dir / f"{filename}.pkl"
        logger.info(f"Checking for cached file: {cached_file}")
        if not cached_file.exists():
            return None
        try:
            with open(cached_file, 'rb') as handle:
                data = pickle.load(handle)
            logger.debug("Data loaded successfully from cache")
            return data
        except Exception as e:
            logger.error(f"Failed to load cached data: {e}")
            return None
    def save_to_cache(self, df: pd.DataFrame, filename: str):
        cached_file = self.cache_dir / f"{filename}.pkl"
        try:
            with open(cached_file, 'wb') as handle:
                pickle.dump(df, handle)
            logger.info(f"Cached data successfully at {cached_file}")
        except Exception as e:
            logger.error(f"Failed to save cached data: {e}")
    def process_data(self, df: pd.DataFrame):
        logger.info("Starting core processing...")
        processed_df = df.copy()
        try:
            mean_val = processed_df['value'].mean()
            std_val = processed_df['value'].std()
            if std_val == 0:
                logger.warning("Standard deviation is zero, setting normalized value to 1")
                processed_df['normalized_value'] = np.where(processed_df['value'] > mean_val, 1.0, -1.0)
            else:
                processed_df['normalized_value'] = (processed_df['value'] - mean_val) / std_val
            logger.info(f"Processing complete. Mean={mean_val:.4f}, Std={std_val:.4f}")
        except Exception as e:
            logger.error("Error during core processing")
            raise
    def run(self, input_file_path=None):
        if input_file_path is None or not Path(input_file_path).exists():
            raw_data = pd.DataFrame({
                'id': [101, 102, 103],
                'value': [5.0, -2.0, np.nan]
            })
        else:
            logger.info(f"Loading data from {input_file_path}")
            raw_data = pd.read_csv(input_file_path)
        if not self.validate_data(raw_data):
            raise ValueError("Data validation failed")
        cached_df = self.load_from_cache('sample')
        logger.info(f"Cache status: {cached_df is not None}")
        if cached_df is not None and raw_data.shape[0] == 3:                                                   
            logger.warning("Using existing cached data")
            df_to_process = cached_df.copy()
        else:
            self.save_to_cache(raw_data, 'sample')
            df_to_process = raw_data
        try:
            self.process_data(df_to_process)
            logger.info("Pipeline execution completed successfully")
            final_df_name = 'processed_sample'
            self.save_to_cache(df_to_process, final_df_name)
        except Exception as e:
            logger.critical(f"Critical error in pipeline execution: {e}")
if __name__ == '__main__':
    pipeline = DataPipeline()
    try:
        pipeline.run(input_file_path=None)
    except Exception as e:
        logger.critical(f"Pipeline failed due to exception: {e}")