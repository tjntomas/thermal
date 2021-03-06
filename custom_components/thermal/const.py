"""Constants for integration."""

DOMAIN = "thermal"

VERSION = "1.0.0"
ISSUE_URL = "https://github.com/eyalcha/thermal/issues"

CONF_WIDTH = "width"
CONF_HEIGHT = "height"
CONF_MIN_TEMPERATURE = "min_temp"
CONF_MAX_TEMPERATURE = "max_temp"
CONF_METHOD = "method"
CONF_ROI = "roi"
CONF_TOP = "top"
CONF_LEFT = "left"
CONF_RIGHT = "right"
CONF_BOTTOM = "bottom"
CONF_STATE = "state"
CONF_SENSOR = "sensor"
CONF_ROWS = "rows"
CONF_COLS = "cols"
CONF_ROTATE = "rotate"
CONF_MIRROR = "mirror"
CONF_FORMAT = "format"
CONF_INTERPOLATE = "interpolate"
CONF_COLD_COLOR = "cold_color"
CONF_HOT_COLOR = "hot_color"

DEFAULT_NAME = "Thermal"
DEFAULT_VERIFY_SSL = False
DEFAULT_IMAGE_WIDTH = 640
DEFAULT_IMAGE_HEIGHT = 640
DEFAULT_MIN_TEMPERATURE = 26.0
DEFAULT_MAX_TEMPERATURE = 32.0
DEFAULT_METHOD = "bicubic"
DEFAULT_STATE = "average"
DEFAULT_ROWS = 8
DEFAULT_COLS = 8
DEFAULT_ROTATE = 0
DEFAULT_MIRROR = False
DEFAULT_COLD_COLOR = "indigo"
DEFAULT_HOT_COLOR = "red"
DEFAULT_FORMAT = "jpeg"

SERVICE_AUTO_SCALE = "auto_scale"

SESSION_TIMEOUT = 1
