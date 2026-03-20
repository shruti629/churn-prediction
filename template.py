import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


project_name = "churn_prediction"

list_of_files = [
    # ── CI/CD ──────────────────────────────────────────────
    ".github/workflows/.gitkeep",

    # ── Source package ─────────────────────────────────────
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    # ── Pipeline stages ────────────────────────────────────
    f"src/{project_name}/components/data_extraction.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/feature_engineering.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",

    # ── Pipeline runners ───────────────────────────────────
    f"src/{project_name}/pipeline/stage_01_data_extraction.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_feature_engineering.py",
    f"src/{project_name}/pipeline/stage_05_model_trainer.py",
    f"src/{project_name}/pipeline/stage_06_model_evaluation.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/batch_score_pipeline.py",

    # ── Entity (dataclasses for config) ────────────────────
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",

    # ── Data sources ───────────────────────────────────────
    f"src/{project_name}/components/sources/__init__.py",
    f"src/{project_name}/components/sources/salesforce_source.py",
    f"src/{project_name}/components/sources/postgres_source.py",
    f"src/{project_name}/components/sources/zendesk_source.py",
    f"src/{project_name}/components/sources/stripe_source.py",
    f"src/{project_name}/components/sources/label_builder.py",

    # ── Monitoring ─────────────────────────────────────────
    f"src/{project_name}/components/monitor.py",

    # ── Configs ────────────────────────────────────────────
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    ".env.example",

    # ── Data directories (gitkeep = tracked but empty) ─────
    "data/raw/.gitkeep",
    "data/validated/.gitkeep",
    "data/processed/.gitkeep",
    "data/features/.gitkeep",
    "data/scores/.gitkeep",

    # ── Models + references ────────────────────────────────
    "models/.gitkeep",
    "references/.gitkeep",

    # ── Airflow DAG ────────────────────────────────────────
    "airflow/dags/churn_weekly_dag.py",

    # ── Dashboard ──────────────────────────────────────────
    "dashboard/app.py",
    "dashboard/requirements.txt",

    # ── Research notebooks ─────────────────────────────────
    "research/01_eda.ipynb",
    "research/02_feature_analysis.ipynb",
    "research/03_experiment_analysis.ipynb",

    # ── Tests ──────────────────────────────────────────────
    "tests/__init__.py",
    "tests/test_features.py",
    "tests/test_api.py",
    "tests/test_pipeline.py",

    # ── Root files ─────────────────────────────────────────
    "main.py",
    "app.py",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "dvc.yaml",
    "README.md",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}  for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filename}")