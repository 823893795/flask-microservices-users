class BaseConfig:
    DEBUG = False
    Testing = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    Testing = True


class ProductionConfig(BaseConfig):
    DEBUG = False