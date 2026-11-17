import contextlib
import functools
import io
import json
import math
import os
import sys
import threading

G = 9.80665 #ms^-2

ENGINE_LOCK = threading.RLock()  

DEFAULTS = {
  "rho": 998.2, #water density @ 20 degrees C 
  "nu": 1.004e-6,  #value for water at 20 degrees C 
  "p_atm_kpa": 101.3,  #atmospheric pressure in kPa
  "p_vap_kpa": 2.339, #vapour pressure of water at 20 degrees C 
  "river_level": 630.0, #in meters at the WORST case scenario!
  "pump_z": 632.0, #pump centerline
  
