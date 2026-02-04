"""Shared platform configurations for quadrotor control."""

from .platform_interface import (
    PlatformType,
    PlatformConfig,
    PLATFORM_REGISTRY,
)

__all__ = [
    'PlatformType',
    'PlatformConfig',
    'PLATFORM_REGISTRY',
]
