activate_this = 'D:/First-oscar-project/oscar/Scripts/activate.bat'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('D:/First-oscar-project/oscar/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('D:/First-oscar-project/AhsanShop')
sys.path.append('D:/First-oscar-project/AhsanShop/AhsanShop')

os.environ['DJANGO_SETTINGS_MODULE'] = 'AhsanShop.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AhsanShop.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()