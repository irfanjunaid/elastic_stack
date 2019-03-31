import elasticapm
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

# initialize using environment variables from elasticapm.contrib.flask import ElasticAPM
app = Flask(__name__)

# configure to use ELASTIC_APM in your application's settings from elasticapm.contrib.flask import ElasticAPM
app.config['ELASTIC_APM'] = {
    # allowed app_name chars: a-z, A-Z, 0-9, -, _, and space from elasticapm.contrib.flask
    'APP_NAME': 'flask-apm-client',
    'DEBUG': True,
    'SERVER_URL': 'http://localhost:8200',
    'TRACES_SEND_FREQ': 5,
    'SERVICE_NAME': 'flaskapp',
    'FLUSH_INTERVAL': 1, # 2.x
    'MAX_QUEUE_SIZE': 1, # 2.x
    'TRANSACTIONS_IGNORE_PATTERNS': ['.*healthcheck']
}
apm = ElasticAPM(app, logging=True)

@app.route('/')
def foo_route():
    return foo()

@elasticapm.capture_span()
def foo():
    return "foo"

if __name__ == '__main__':
    app.run()
