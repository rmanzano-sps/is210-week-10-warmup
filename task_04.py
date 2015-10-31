#!/usr/bin/env coding
# -*- coding: utf-8 -*-
"""Using .update() for merging  dictionaries"""

import data

data.BANDS['Buckingham Nicks'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                                  'Stevie Nicks': ['vocals', 'tambourine']}

data.BANDS['Fleetwood Mac'].update(data.BANDS['Buckingham Nicks'])
