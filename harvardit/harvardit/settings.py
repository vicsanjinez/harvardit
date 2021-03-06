"""
Django settings for harvardit project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q^%n-tc#sqwk$*bzccl@foufciljlqu5dm*6ht@sh!+uu%tzf!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
                'localhost',
                '127.0.0.1',
                ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'harvardit',
    'bootstrap4',
    'web3',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'harvardit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'harvardit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s >>>>> %(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
                 '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': BASE_DIR + '/log/django-harvardit.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile', 'console', 'mail_admins',],
            'level': 'INFO',
            'propagate': True,
        },
        'harvardit': {
            'handlers': ['logfile', 'console', 'mail_admins',],
            'level': 'DEBUG',
        }
    },
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static-hyperledger_traceit/static'

LOGIN_URL = '/'


SC_ABI = '[{"constant":true,"inputs":[],"name":"subjectsCompleted","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"subject","type":"int8"},{"name":"theGrade","type":"int8"}],"name":"setGrade","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"degreeObtained","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"professorAddress","type":"address"}],"name":"setProfessor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"thesis","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"professors","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"thesisHash","type":"bytes32"}],"name":"registerThesis","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"int8"}],"name":"grades","outputs":[{"name":"","type":"int8"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'
SC_BYTECODE = '0x608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff600160008060000b815260200190815260200160002060006101000a81548160ff021916908360000b60ff1602179055507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60016000600160000b815260200190815260200160002060006101000a81548160ff021916908360000b60ff1602179055507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60016000600260000b815260200190815260200160002060006101000a81548160ff021916908360000b60ff1602179055506000600360006101000a81548160ff0219169083151502179055506000600360016101000a81548160ff02191690831515021790555061066b8061018e6000396000f300608060405260043610610099576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063164afb271461009e57806322fecf09146100cd57806357244b471461010a57806375b1c531146101395780638da5cb5b1461017c578063a03e9608146101d3578063cd1e9e2b14610206578063d829bc4714610261578063de28b85814610292575b600080fd5b3480156100aa57600080fd5b506100b36102dc565b604051808215151515815260200191505060405180910390f35b3480156100d957600080fd5b50610108600480360381019080803560000b9060200190929190803560000b90602001909291905050506102ef565b005b34801561011657600080fd5b5061011f61038f565b604051808215151515815260200191505060405180910390f35b34801561014557600080fd5b5061017a600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506103a2565b005b34801561018857600080fd5b50610191610458565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101df57600080fd5b506101e861047d565b60405180826000191660001916815260200191505060405180910390f35b34801561021257600080fd5b50610247600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610483565b604051808215151515815260200191505060405180910390f35b34801561026d57600080fd5b5061029060048036038101908080356000191690602001909291905050506104a3565b005b34801561029e57600080fd5b506102c0600480360381019080803560000b9060200190929190505050610549565b604051808260000b60000b815260200191505060405180910390f35b600360009054906101000a900460ff1681565b60011515600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16151514151561034e57600080fd5b80600160008460000b60000b815260200190815260200160002060006101000a81548160ff021916908360000b60ff16021790555061038b610569565b5050565b600360019054906101000a900460ff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156103fd57600080fd5b6001600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff02191690831515021790555050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60045481565b60026020528060005260406000206000915054906101000a900460ff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156104fe57600080fd5b60011515600360009054906101000a900460ff16151514151561052057600080fd5b80600481600019169055506001600360016101000a81548160ff02191690831515021790555050565b60016020528060005260406000206000915054906101000a900460000b81565b6005600160008060000b815260200190815260200160002060009054906101000a900460000b60000b121580156105c85750600560016000600160000b815260200190815260200160002060009054906101000a900460000b60000b12155b80156105fc5750600560016000600260000b815260200190815260200160002060009054906101000a900460000b60000b12155b15610621576001600360006101000a81548160ff02191690831515021790555061063d565b6000600360006101000a81548160ff0219169083151502179055505b5600a165627a7a723058203a47828fe163ba7cf0f3f3228cc2c2c7982a5bd2f43d56303d0f13cfd822dc840029'