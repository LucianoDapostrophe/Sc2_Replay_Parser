import argparse, sys, sc2reader
from sc2reader.events.game import *
from sc2reader.events.message import *
from sc2reader.events.tracker import *

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('DirectoryName', type=str, help="the directory to parse")
    parser.add_argument('Sample_Window', type=int, help="15, 30, or 45")

    args = parser.parse_args()
    
    dictionary = {}
    id = 1
    maxSeconds = 600
    windowSeconds = args.Sample_Window