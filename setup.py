from cx_Freeze import setup, Executable
import os

# Añadir aquí la lista de archivos adicionales que tu aplicación necesita
includefiles = [
    'coco.names',
    'frozen_inference_graph.pb',
    'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt',  # Correct path here
]
# Aquí se define el script Python principal
executables = [Executable('main.py', base=None)]

# Definir el setup
setup(
    name="Detector de Objetos",
    version="1.0",
    description="Detector de objetos utilizando TensorFlow y OpenCV",
    options={"build_exe": {"include_files": includefiles}},  # Incluir archivos adicionales
    executables=executables,
)