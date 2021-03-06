# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/app/reverse/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/app/reverse/config.proto',
  package='v2ray.core.app.reverse',
  syntax='proto3',
  serialized_options=_b('\n\034com.v2ray.core.proxy.reverseP\001Z\007reverse\252\002\030V2Ray.Core.Proxy.Reverse'),
  serialized_pb=_b('\n\'v2ray.com/core/app/reverse/config.proto\x12\x16v2ray.core.app.reverse\"o\n\x07\x43ontrol\x12\x34\n\x05state\x18\x01 \x01(\x0e\x32%.v2ray.core.app.reverse.Control.State\x12\x0e\n\x06random\x18\x63 \x01(\x0c\"\x1e\n\x05State\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\t\n\x05\x44RAIN\x10\x01\"+\n\x0c\x42ridgeConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\"+\n\x0cPortalConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\"\x82\x01\n\x06\x43onfig\x12;\n\rbridge_config\x18\x01 \x03(\x0b\x32$.v2ray.core.app.reverse.BridgeConfig\x12;\n\rportal_config\x18\x02 \x03(\x0b\x32$.v2ray.core.app.reverse.PortalConfigBD\n\x1c\x63om.v2ray.core.proxy.reverseP\x01Z\x07reverse\xaa\x02\x18V2Ray.Core.Proxy.Reverseb\x06proto3')
)



_CONTROL_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='v2ray.core.app.reverse.Control.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAIN', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=148,
  serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_CONTROL_STATE)


_CONTROL = _descriptor.Descriptor(
  name='Control',
  full_name='v2ray.core.app.reverse.Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='v2ray.core.app.reverse.Control.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random', full_name='v2ray.core.app.reverse.Control.random', index=1,
      number=99, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTROL_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=178,
)


_BRIDGECONFIG = _descriptor.Descriptor(
  name='BridgeConfig',
  full_name='v2ray.core.app.reverse.BridgeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.reverse.BridgeConfig.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='v2ray.core.app.reverse.BridgeConfig.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=223,
)


_PORTALCONFIG = _descriptor.Descriptor(
  name='PortalConfig',
  full_name='v2ray.core.app.reverse.PortalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.reverse.PortalConfig.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='v2ray.core.app.reverse.PortalConfig.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=268,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.reverse.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bridge_config', full_name='v2ray.core.app.reverse.Config.bridge_config', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portal_config', full_name='v2ray.core.app.reverse.Config.portal_config', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=401,
)

_CONTROL.fields_by_name['state'].enum_type = _CONTROL_STATE
_CONTROL_STATE.containing_type = _CONTROL
_CONFIG.fields_by_name['bridge_config'].message_type = _BRIDGECONFIG
_CONFIG.fields_by_name['portal_config'].message_type = _PORTALCONFIG
DESCRIPTOR.message_types_by_name['Control'] = _CONTROL
DESCRIPTOR.message_types_by_name['BridgeConfig'] = _BRIDGECONFIG
DESCRIPTOR.message_types_by_name['PortalConfig'] = _PORTALCONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Control = _reflection.GeneratedProtocolMessageType('Control', (_message.Message,), dict(
  DESCRIPTOR = _CONTROL,
  __module__ = 'v2ray.com.core.app.reverse.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.reverse.Control)
  ))
_sym_db.RegisterMessage(Control)

BridgeConfig = _reflection.GeneratedProtocolMessageType('BridgeConfig', (_message.Message,), dict(
  DESCRIPTOR = _BRIDGECONFIG,
  __module__ = 'v2ray.com.core.app.reverse.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.reverse.BridgeConfig)
  ))
_sym_db.RegisterMessage(BridgeConfig)

PortalConfig = _reflection.GeneratedProtocolMessageType('PortalConfig', (_message.Message,), dict(
  DESCRIPTOR = _PORTALCONFIG,
  __module__ = 'v2ray.com.core.app.reverse.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.reverse.PortalConfig)
  ))
_sym_db.RegisterMessage(PortalConfig)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'v2ray.com.core.app.reverse.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.reverse.Config)
  ))
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
