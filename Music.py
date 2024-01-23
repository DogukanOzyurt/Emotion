import mido
from mido import MidiFile, MidiTrack, Message
import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def create_midi_file(notes, output_file="output.mid"):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for note in notes:
        track.append(Message('note_on', note=note, velocity=64, time=100))
        track.append(Message('note_off', note=note, velocity=64, time=100))

    mid.save(output_file)

# Example notes: C, D, E, F, G, A, B
# Corresponding MIDI note numbers: 60, 62, 64, 65, 67, 69, 71
notes_to_play = [60, 62, 64, 65, 67, 69, 71]

# Create the MIDI file
create_midi_file(notes_to_play)

# Play the MIDI file
play_music("output.mid")
