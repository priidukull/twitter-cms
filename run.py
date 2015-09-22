#!flask/bin/python
import os
from app import app

if __name__ == '__main__':
    env = os.environ.get('ENVIRONMENT')
    if env == 'twitter':
        app.run('0.0.0.0', 80)
    else:
        app.run(debug=True)
